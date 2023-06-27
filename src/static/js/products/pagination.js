import { sendSync, buildGetRequest } from "../helpers/request.js";


export default class Pagination {
    constructor(createListCb, url, scrollToDivId) {
        this.scrollToDivId = scrollToDivId;
        this.createListCb = createListCb,
        this.url = url,
        this.page = 1,
        this.params = {
            page: 'page',
            items: 'items',
        },
        this.items = {
            small: 8,
            medium: 12
        }
        this.screen = {
            medium: 768,
        }
        this.wScreen = window.innerWidth;
        this.elements = {
            paginationDiv: document.getElementById('pagination'),
            pageContainer: document.querySelector('#pagination .page-container'),
            previousLink: null,
            nextLink: null
        }
    }
 
    setParams = function(url) {
       const items = this._getNumberOfItems();
       const pageQuery = `${this.params.page}=${this.page}`;
       const itemsQuery = `${this.params.items}=${items}`;
       return `${url}?${pageQuery}&${itemsQuery}`;
    }
 
    buildHtml = function(paginationObj) {
        const hide = this._hideIfHasOnlyOneLink(paginationObj.numPages);
        if (!hide) {
            this._buildLinks(paginationObj.numPages);
            this._loadLinkEvents();
            this._setStyles(paginationObj);
        } 
    }

    _getNumberOfItems = function() {
        const items = (this.wScreen < this.screen.medium)? this.items.small : this.items.medium;
        return items;
    }

    _hideIfHasOnlyOneLink = function(numberPages) {
        const hide = (numberPages === 1);
        if(hide) {
            this.elements.paginationDiv.classList.add('d-none');
        }  
        return hide;
    }

    _buildLinks = function(numPages) {
        this.elements.pageContainer.innerHTML = this._buildInitialElements();
        this._loadPreviousAndNext();

        for(let i = 2; i <= numPages; i++) {
            const li = document.createElement('li');
            li.classList.add('page-link');
            li.innerText = i;
            li.setAttribute('data-page', i);
            this.elements.pageContainer.insertBefore(li, this.elements.nextLink);
        }
    }

    _buildInitialElements = function() {
        return `
            <li class="page-link previous disabled"><i class="bi bi-chevron-double-left"></i></li>
            <li class="page-link current" data-page="1">1</li>
            <li class="page-link next"><i class="bi bi-chevron-double-right"></i></li>
        `
    }

    _loadPreviousAndNext = function() {
        this.elements.previousLink =document.querySelector('#pagination .previous');
        this.elements.nextLink = document.querySelector('#pagination .next');
    }

    _loadLinkEvents =  function() {
        const pageLinks = this._getPageLinks();
        const { previous, next } = this._getPreviousAndNext();

        pageLinks.forEach(link => link.onclick = e => this._clickInLink(e));
        previous.onclick = e => this._clickInPrevious(e);
        next.onclick = e => this._clickInNext(e)
    }

    _clickInLink = function(e) {
        const link = e.target.closest('.page-link');
        const page = link.getAttribute('data-page');
        this._setPage(page);
        this._getItems();
    }

    _clickInPrevious = function(e) {
        const previous = e.target.closest('.page-link.previous');
        const previousPage = previous.getAttribute('data-previous-page');
        const link = this.elements.pageContainer.querySelector(`li[data-page="${previousPage}"]`);
        link.click();
    }

    _clickInNext = function(e) {
        const next = e.target.closest('.page-link.next');
        const nextPage = next.getAttribute('data-next-page');
        const link = this.elements.pageContainer.querySelector(`li[data-page="${nextPage}"]`);
        link.click();
    }
    
    _setPage = function(page) {
        this.page = page;
    }

    _getItems = async function() {
        const url = this.setParams(this.url);
        const req = buildGetRequest();
        const res = await sendSync(req, url);
        this.createListCb(res.obj.products, null);
        this._setStyles(res.obj.pagination);
        this._scrollToProductSection();
    }

    _setStyles = function(paginationObj) {
        const pageLinks = this._getPageLinks();
        const currentLink = this.elements.pageContainer.querySelector(`li[data-page="${this.page}"]`);
        const { previous, next } = this._getPreviousAndNext();
        pageLinks.forEach(link => link.classList.remove('current'));
        currentLink.classList.add('current');

        if (paginationObj.hasPrevious) {
            previous.classList.remove('disabled');
            previous.setAttribute('data-previous-page', parseInt(this.page) - 1);
        } else {
            previous.classList.add('disabled');
            previous.setAttribute('data-previous-page', '-');
        }

        if (paginationObj.hasNext) {
            next.classList.remove('disabled');
            next.setAttribute('data-next-page', parseInt(this.page) + 1);
        } else {
            next.classList.add('disabled');
            next.setAttribute('data-next-page', '-');
        }
    }

    _getPageLinks = function() {
        const pageLinks = this.elements.pageContainer.querySelectorAll('.page-link:not(.previous):not(.next)');
        return pageLinks;
    }

    _getPreviousAndNext = function() {
        const previous = this.elements.pageContainer.querySelector('.page-link.previous');
        const next = this.elements.pageContainer.querySelector('.page-link.next');
        return {previous, next};
    }

    _scrollToProductSection = function() {
        const scrollToDiv = document.getElementById(this.scrollToDivId);
        scrollToDiv.scrollIntoView();
    }
}