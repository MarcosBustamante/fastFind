/**
 * Created by iury on 3/5/15.
 */
angular.module('FastFindApp', ['FastFindApi', 'ui.bootstrap']);

angular.module('FastFindApp').config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
});
