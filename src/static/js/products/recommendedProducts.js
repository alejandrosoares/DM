import productApi from "../apis/productApi.js";


class RecommendedSection {

    constructor() {
        this.mainProductContainer = document.querySelector('.main-product');
        this.recommendationContainer = document.querySelector('.recommendations .products-list');
        this.recommendationWrapper = this.recommendationContainer.querySelector('.row');
        this.template = document.getElementById('template-product-card');
        this.productId = this.mainProductContainer.getAttribute('data-product-id');
        this.limit = 4;
        this.loaderContainer = document.querySelector('.products-loader');
    }

    async buildHTML() {
        await this._buildRecommendationList();
        this._disableLoader();
    }

    _disableLoader() {
        this.loaderContainer.classList.add('d-none');
    }

    async _buildRecommendationList() {
        const products = await this._fetchProducts();
        products.forEach(product => {
            const productHTML = this._buildProductHTML(product);
            this.recommendationWrapper.appendChild(productHTML);
        });
        this.recommendationContainer.classList.remove('d-none');
    }

    _buildProductHTML(productData) {
        const product = this.template.content.cloneNode(true);
        const productImg = product.querySelector('img');
        const productName = product.querySelector('.name > span');
        const productPrice = product.querySelector('.price > span');

        productImg.src = productData.img.url;
        productImg.width = productData.img.width;
        productImg.heigth = productData.img.heigth;
        productName.textContent = productData.name;
        productPrice.textContent = `CHF ${productData.price}`;
        product.href = productData.url;

        return product;
    }

    async _fetchProducts() {
        const response = await productApi.getRecommendedProducts(
            this.productId, 
            this.limit
        );
        return response.data.obj;
    }
}


async function loadRecommendedProducts() {
    const recommendedSection = new RecommendedSection();
    await recommendedSection.buildHTML();
}


loadRecommendedProducts();