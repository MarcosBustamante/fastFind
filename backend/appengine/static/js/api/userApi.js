/**
 * Created by bustamante on 4/27/15.
 */
angular.module('FastFindApp').factory('UserApi', function(Ajax){
    var url_save = "/cadastro/usuarios/salvar";
    var url_login = "/login/home/sing_in";


    var save = function(form){
        var parameters = {'form': angular.toJson(form)};
        return Ajax.post(url_save, parameters)
    };

    var logar = function(login, password){
        var parameters = {
            'login': login,
            'password': password
        };
        return Ajax.post(url_login, angular.toJson(parameters))
    };

    return {
        save: save,
        logar: logar
    }
});