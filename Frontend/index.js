angular.module("user_login_cookie",['ngCookies']).controller("user_login_ctrl_cookie",function($scope,$http,$cookies){

    $scope.subFunction=function(){
        
        console.log($scope.email);
        sessionStorage.setItem("mail",$scope.email);
        
      
            $cookies.put('cookie',sessionStorage.getItem('mail'));


            $scope.mycookieval=$cookies.get('cookie');
    
        var data={"email":$scope.email,"password":$scope.password}

        $http.post('http://127.0.0.1:8000/amazing/user/login/', JSON.stringify(data)).then(function (response) {
            if(response.data=="wrong")
            alert("wrong credentials");
            else{
            sessionStorage.setItem("cust_id",response.data['id']);
            window.location.href="website.html";
            }
    });
    }
    
})