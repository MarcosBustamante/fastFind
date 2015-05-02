/**
 * Created by bustamante on 4/27/15.
 */
angular.module('FastFindApp').controller('LoginCtrl', function($scope, UserApi, $timeout){
    $scope.form = {};

    var _validate = function(form){
        var errors = {};
        if(form == undefined)
            form = {};
        if(form.login == undefined || form.login == '')
            errors['login'] = 'Campo obrigatório';
        if(form.email == undefined || form.email == '')
            errors['email'] = 'Campo obrigatório';
        else if(form.email.indexOf('@') < 0 || form.email.indexOf('.') < 0 )
            errors['email'] = 'Email inválido';
        if(form.password == undefined || form.password == '')
            errors['password'] = 'Campo obrigatório';
        if(form.password2 == undefined || form.password2 == '')
            errors['password2'] = 'Campo obrigatório';
        if(form.password2 && form.password && form.password2 != form.password){
            errors['password2'] = 'As senhas estão diferentes';
            errors['password'] = 'As senhas estão diferentes';
        }
        return errors;
    };

    $scope.register = function(){
        var errors = _validate($scope.form);
        if(!jsutils.object_is_empty(errors)){
            $scope.form['errors'] = errors;
        } else {
            delete $scope.form.errors;
            UserApi.save($scope.form).success(function(result){
                $scope.form = {};
                $scope.successAlert = true;
            }).error(function(error){
                $scope.dadosInvalidosCadastro = true;
            });

            $timeout(function(){
                $scope.successAlert = false;
                $scope.dadosInvalidosCadastro = false;
            }, 10000);
        }
    };

    $scope.singIn = function(){
        if( $scope.login === undefined || $scope.login === '' || $scope.password === undefined || $scope.password === '')
            $scope.camposObrigatorios = true;
        else {
            UserApi.logar($scope.login, $scope.password).success(function (result) {
                FF.user = result;
                $scope.successLoginAlert = true;
                $timeout(function(){
                    $scope.successLoginAlert= false;
                }, 10000);
            }).error(function(erro){
                $scope.dadosInvalidos = true;
            });
        }
    };

    $scope.closePopup = function(){
        $scope.camposObrigatorios = $scope.dadosInvalidos = false;
    };

    $scope.removeError = function(index){
        if($scope.form.errors !== undefined && index in $scope.form.errors)
            delete $scope.form.errors[index]
    };
});
