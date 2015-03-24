/**
 * Created by iury on 3/8/15.
 */
angular.module('FastFindApp').factory('ProductModel', function(){
    var products;
    var selectedProduct;

    var select = function(product){
        if(selectedProduct !== undefined)
            selectedProduct.selected = false;
        product.selected = true;
        selectedProduct = product
    };

    var getSelectedProduct = function(){
        return selectedProduct;
    };
    
    var find = function(label){
        var base = '/static/img/product/xbox';
        products = [
            {
                'id': 1,
                'name':'X-box One 1',
                'images':[base+'1.jpg',base+'2.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 2,
                'name':'X-box One 2',
                'images':[base+'2.jpg',base+'1.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 3,
                'name':'X-box One 3',
                'images':[base+'1.jpg',base+'2.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 4,
                'name':'X-box One 4',
                'images':[base+'2.jpg',base+'1.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 5,
                'name':'X-box One 5',
                'images':[base+'1.jpg',base+'2.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 6,
                'name':'X-box One 6',
                'images':[base+'2.jpg',base+'1.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 7,
                'name':'X-box One 7',
                'images':[base+'1.jpg',base+'2.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 8,
                'name':'X-box One 8',
                'images':[base+'2.jpg',base+'1.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 9,
                'name':'X-box One 9',
                'images':[base+'1.jpg',base+'2.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            },
            {
                'id': 10,
                'name':'X-box One 10',
                'images':[base+'2.jpg',base+'1.jpg',base+'3.jpg'],
                'logo':'/static/img/product/americanas.jpg',
                'distance':'500m',
                'price':'R$ 2.230,00',
                'shopName':'Loja do Jão',
                'street':'Rua 1 - 158, Centro',
                'comment':[]
            }
        ];

        select(products[0]);
        return products;
    };

    return {
        find: find,
        select: select,
        getSelectedProduct: getSelectedProduct,
        marcos: selectedProduct
    }
});
