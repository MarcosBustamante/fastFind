/**
 * Created by iury on 3/8/15.
 */
angular.module('FastFindApi', ['ajax']);
angular.module('FastFindApi').factory('ProductApi', function(Ajax){
    var url_list = '/api/product/listing';

    var list = function(){
        return Ajax.get(url_list)
    }

    return {
        list: list
    }
});
