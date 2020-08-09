angular.module("user_logout",[]).controller("user_logout_ctrl",function($scope,$http){
$scope.subFunction=function(){
        
        
    $http.get('http://127.0.0.1:8000/amazing/user/logout/').then(function (response) {
        if(response.data)
        alert(response.data);
        
},function(){
        alert("error");
});
}
})