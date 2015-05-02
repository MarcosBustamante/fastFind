/**
 * Created by bustamante on 4/6/15.
 */
angular.module('FastFindApp').factory('StoreCrud', function(Ajax){
    var selectedShop;
    var shops = [];

    var _getEmptyForm = function(){
        return {
            image: undefined,
            name: undefined,
            address: undefined,
            number: undefined,
            district: undefined,
            city: undefined,
            errors:{}
        }
    };

    var validateForm = function(form){
        var errors = {};
        if(form.name === undefined || form.name === ''){
            errors.name='Campo obrigatório';
        }
        if(form.address === undefined || form.address === ''){
            errors.address='Campo obrigatório';
        }
        if(form.number === undefined || form.number === ''){
            errors.number='Campo obrigatório';
        }else if(isNaN(form.number)){
            errors.number='Insira apenas números';
        }
        if(form.district === undefined || form.district === ''){
            errors.district='Campo obrigatório';
        }
        if(form.city === undefined || form.city === ''){
            errors.city='Campo obrigatório';
        }
        return errors;
    };

    var _list = function(){
        Ajax.get("/cadastro/lojas/listar").success(function(result){
            if(typeof result === "object"){
                shops = result;
            }
        }).error(function(error){
            console.error(error);
        });
    };

    var _latlong = [0, 0];
    var geoSuccess = function(position) {
        _latlong = [position.coords.latitude, position.coords.longitude];
    };

    var save = function(form){
        if(navigator.geolocation !== undefined)
            navigator.geolocation.getCurrentPosition(geoSuccess);

        form["latitude"] = _latlong[0];
        form["longitude"] = _latlong[1];

        if(jsutils.object_is_empty(form.errors)) {
            delete form['errors'];
            var parameters = {'form': angular.toJson(form)};
            Ajax.post('/cadastro/lojas/salvar', parameters).success(function(result){
                if(!jsutils.object_is_empty(result)) {
                    shops.push(result);
                }
            });
        }
    };

    var remove = function(shop_id){
        Ajax.post("/cadastro/lojas/deletar", {'id': shop_id}).success(function(result){
            for(var i = 0; i < shops.length; ++i) {
                if (shops[i]['id'] == shop_id) {
                    shops.splice(i, 1);
                }
            }
            selectedShop = _getEmptyForm();
        }).error(function(error){
            console.error(error);
        });
    };

    var select = function(index){
        if(index == -1)
            selectedShop = _getEmptyForm();
        else
            selectedShop = shops[index];
    };

    var init = function(){
        selectedShop = _getEmptyForm();
        shops = _list();
    };

    var getShops = function(){
        return shops;
    };

    var getSelectedShop = function(){
        return selectedShop;
    };

   return {
       validateForm: validateForm,
        getSelectedShop: getSelectedShop,
        getShops: getShops,
        save: save,
        remove: remove,
        select: select,
        init: init
   }
});

angular.module('FastFindApp').controller('RegisterStoreCtrl', function($scope, StoreCrud, $timeout){
    var scrud = $scope.scrud = StoreCrud;
    scrud.init();

    $scope.form = scrud.getSelectedShop();

    $scope.save = function(){
        var errors = scrud.validateForm($scope.form);
        $scope.form.errors = errors;

        if(jsutils.object_is_empty(errors)) {
            scrud.save($scope.form);
            $scope.selectShop(-1);
        }
    };

    $scope.remove = function(){
        scrud.remove($scope.form.id);
        $scope.selectShop(-1);
    };

    $scope.selectShop = function(index){
        scrud.select(index);
        $scope.form = scrud.getSelectedShop();
    };

    $scope.removeError = function(formName){
        if($scope.form.errors)
            delete $scope.form.errors[formName];
    };
});
