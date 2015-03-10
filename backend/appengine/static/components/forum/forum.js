angular.module('FastFindApp').directive('forum', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/components/forum/forum.html',
        scope: {
            comments: '='
        },
        controller: function($scope, $rootScope){
            $scope.FF = window.FF;

            $scope.saveComment = function(){
                var comment = [{
                    'img':FF.user.avatar,
                    'name':FF.user.name,
                    'lastName':FF.user.lastName,
                    'comment': $scope.comment
                }];
                $scope.comments = comment.concat($scope.comments);
                $scope.dirtyComment();
                $scope.buttonsStatus = false;
            };

            $scope.showButtons = function(){
                $scope.buttonsStatus = true;
            };

            $scope.dirtyComment = function(){
                $scope.comment = '';
            };

//            $scope.deletComment = function(commentIndex){
//                $scope.comments.splice(commentIndex,1);
//            };
//
//            $scope.updateComment = function(comment){
//                comment.comment = comment.editComment;
//                comment.isEdit = false;
//            };
//
//            $scope.cancelOrEdit = function(comment){
//                comment.isEdit = !comment.isEdit;
//                comment.editComment = comment.isEdit ? comment.comment: '';
//            }
        }
    }
});