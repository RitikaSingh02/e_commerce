angular.module("user_login",[]).controller("user_login_ctrl",function($scope,$http){

    $scope.subFunction=function(){
        console.log($scope.email);
        var data={"email":$scope.email,"password":$scope.password}
        $http.post('http://127.0.0.1:8000/amazing/user/login/', JSON.stringify(data)).then(function (response) {
            if(response.data=="wrong")
            alert("wrong credentials");
            else{
            window.open("website.html",
            "_blank");
            }
    });
    }
    
})