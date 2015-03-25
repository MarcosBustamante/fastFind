/**
 * Created by bustamante on 3/5/15.
 */
angular.module('FastFindApp', ['ui.bootstrap']);

angular.module('FastFindApp').config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
});
