/**
 * Created by bustamante on 4/6/15.
 */
angular.module('FastFindApp').factory('ProductCrud', function(Ajax){
    var selectedProduct;
    var products = [];
    var stores = [{name: "marcos"}];

    var skeletonProduct = {
        images: ['', '', '', '', '', ''],
        name: undefined,
        price: undefined,
        description: undefined,
        store: undefined,
        errors:{}
    };

    Ajax.get("/cadastro/lojas/listar").success(function(result){
            if(typeof result === "object"){
                stores = result;
            }
        });

    var _getEmptyForm = function(){
        return skeletonProduct;
    };

    var validateForm = function(form){
        var errors = {};
        if(form.name === undefined || form.name === ''){
            errors.name='Campo obrigatório';
        }
        if(form.description === undefined || form.description === ''){
            errors.description='Campo obrigatório';
        }
        if(form.price === undefined || form.price === ''){
            errors.price='Campo obrigatório';
        }
        if(form.store === undefined || form.store === ''){
            errors.store='Campo obrigatório';
        }
        return errors;
    };

    var _list = function(){
        Ajax.get("/cadastro/produtos/listar").success(function(result){
            if(typeof result === "object"){
                for(var i = 0; i < result.length; ++i){
                    while (result[i].images.length < 6) {
                        result[i].images.push('');
                    }
                }
                products = result;
            }
        }).error(function(error){
            console.error(error);
        });
    };

    var save = function(form){
        if(jsutils.object_is_empty(form.errors)) {
            delete form['errors'];
            var parameters = {'form': angular.toJson(form)};
            Ajax.post('/cadastro/produtos/salvar', parameters).success(function(result){
                if(!jsutils.object_is_empty(result)) {
                    products.push(result);
                }
            });
        }
    };

    var remove = function(shop_id, product_id){
        Ajax.post("/cadastro/produtos/deletar", {'shop_id': shop_id, 'product_id': product_id}).success(function(result){
            for(var i = 0; i < products.length; ++i) {
                if (products[i]['id'] == product_id) {
                    products.splice(i, 1);
                }
            }
            selectedProduct = _getEmptyForm();
        }).error(function(error){
            console.error(error);
        });
    };

    var select = function(index){
        if(index == -1)
            selectedProduct = _getEmptyForm();
        else
            selectedProduct = products[index];
    };

    var init = function(){
        selectedProduct = _getEmptyForm();
        _list();
    };

    var getProducts = function(){
        return products;
    };

    var getSelectedProduct = function(){
        return selectedProduct;
    };

    var getStores = function(){
        return stores;
    };

   return {
       validateForm: validateForm,
       getSelectedProduct: getSelectedProduct,
       getProducts: getProducts,
       getStores: getStores,
       save: save,
       remove: remove,
       select: select,
       init: init
   }
});

angular.module('FastFindApp').controller('RegisterProductCtrl', function($scope, ProductCrud){
    var pcrud = $scope.pcrud = ProductCrud;

    pcrud.init();

    $scope.form = pcrud.getSelectedProduct();

    $scope.save = function(){
        var errors = pcrud.validateForm($scope.form);
        $scope.form.errors = errors;

        if(jsutils.object_is_empty(errors)) {
            pcrud.save($scope.form);
            $scope.selectProduct(-1);
        }
    };

    $scope.remove = function(){
        pcrud.remove($scope.form.store, $scope.form.id);
        $scope.selectProduct(-1);
    };

    $scope.selectProduct = function(index){
        pcrud.select(index);
        $scope.form = pcrud.getSelectedProduct();
    };

    $scope.removeError = function(formName){
        if($scope.form.errors)
            delete $scope.form.errors[formName];
    };
});
