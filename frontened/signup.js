angular.module("user_signup",[]).controller("user_signup_ctrl",function($scope,$http){

    $scope.subFunction=function(){
        console.log($scope.email);
        var data={"username":$scope.username,"email":$scope.email,"phone":$scope.phone,"password":$scope.password}
        $http.post('http://127.0.0.1:8000/amazing/user/signup/', JSON.stringify(data)).then(function (response) {
            if(response.data){
                alert("signup")
            }
            
    });
    }
    // $scope.subFunction=function(){
    //     console.log($scope.email);
    //     var data={'email':$scope.email}
    //     $http.post('http://127.0.0.1:8000/amazing/email/',JSON.stringify(data)).then(function (response) {
    //         if(response.data){
    //             alert(response.data)
    //         }
            
    // });
    // }

})