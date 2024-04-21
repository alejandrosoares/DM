import { API_URL } from '../constants/urls.js';
import HttpStatus from '../constants/httpStatus.js';
import buildApiResponseObject from '../helpers/response.js';
import { Request } from '../helpers/request.js';


const productApi = {
    BASE_URL: `http://localhost:8000/products/api/v1`,

    async getRecommendedProducts(productId, limit) {
        const url = `${this.BASE_URL}/recommended-products/${productId}`;
        const req = new Request.Builder(url)
                    .withGetParams({
                        limit 
                    })
                    .build();
        const res = await req.send();
        const data = await res.json();
        return buildApiResponseObject(HttpStatus.OK, res.status, data);
    },
};


export default productApi;