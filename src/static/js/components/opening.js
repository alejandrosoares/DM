import { sendSync } from "../helpers/request.js";
import { getUrl } from "../helpers/url.js";


class OpeningHours extends HTMLElement {
    constructor() {
        super();
        this.isLoaded = false;
        this.shadow = this.attachShadow({ mode: 'open' });
        this.mainChildElement = document.createElement('section');
        this.mainChildElement.classList.add('opening');
        this.openingHoursObj = null;
    }

    getLoadingTemplate() {
        const loadingContent = `
           ${this.getStyles()}
            <div class="col-12 opening-title">
                <h2 class="text-center">Opening hours:</h2>
            </div>
            <div class="col-12 opening-body">
                <img src="/static/img/loader.svg" alt="Loading Image">
                <span class="loading-text">Loading opening hours...</span>
            </div>
        `;
        return loadingContent;
    }

    createSpanMessage(message) {
        const spanContent = `<span>(${message})</span>`;
        return spanContent;
    }

    getLoadedTemplate() {
        const container = document.createElement('div');
        const table = document.createElement('table');
        
        for (const key in this.openingHoursObj) {
            const sch = this.openingHoursObj[key];
            const tr = document.createElement('tr');
            const tdDay = document.createElement('td');
            const tdSchedule = document.createElement('td');

            if(sch.isWeekday) {
                const spanMessage = this.createSpanMessage(sch.open.message);
                tdDay.innerHTML =  `<b>${sch.day}:   </b>`;
                tdSchedule.innerHTML =  `<b>${sch.schedule} ${spanMessage} </b>`;
            } else {
                tdDay.innerHTML =  `${sch.day}:   `;
                tdSchedule.innerHTML =  `${sch.schedule}`;
            }
            tr.appendChild(tdDay);
            tr.appendChild(tdSchedule);  
            table.appendChild(tr);
        }

        container.appendChild(table);

        const loadedContent = `
            ${this.getStyles()}
            <div class="col-12 opening-title">
                <h2 class="text-center">Opening hours:</h2>
            </div>
            <div class="col-12 opening-body">
                ${container.innerHTML}
            </div>
        `;
        return loadedContent;   
    }
    
    getTemplate() {
        this.removeOldRenderOfMain();
        const template = document.createElement('template');
        template.innerHTML = this.isLoaded ? this.getLoadedTemplate() : this.getLoadingTemplate();
        this.mainChildElement.appendChild(template.content.cloneNode(true));
        return this.mainChildElement;
    }

    removeOldRenderOfMain() { 
        while (this.mainChildElement.firstChild) {
            this.mainChildElement.removeChild(this.mainChildElement.firstChild);
        }
    }

    render() {
        this.shadow.appendChild(this.getTemplate());
    }

    async fetchContent() {
        const url = `${getUrl()}/opening/api/v1/`;
        const req = { method: 'GET' };
        const res = await sendSync(req, url);
        if (res.status === 'ok') {
            this.openingHoursObj = res.obj;
            this.isLoaded = true;
            this.render();
        }
    }

    getStyles() {
        return `
            <style>
                :host {
                    display: block;
                    scroll-margin-top: 60px;
                }

                section {
                    display: flex;
                    flex-direction: column;
                    max-width: 600px;
                    margin: auto;
                }

                .opening-title h2 {
                    margin-bottom: .5rem;
                    font-weight: 500;
                    line-height: 1.2;
                    text-align: center;
                    font-size: 2rem;
                }
                
                .opening-body {
                    background-color: var(--white);
                    border: 1px solid var(--border-color);
                    border-radius: 10px;
                    padding: 10px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    scroll-margin-top: 60px;
                }
            </style>
        `;
    }

    connectedCallback() {
        this.render();
        this.fetchContent();
    }
}


customElements.define('opening-hours', OpeningHours);