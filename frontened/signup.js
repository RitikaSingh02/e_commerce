angular.module("user_signup",[]).controller("user_signup_ctrl",function($scope,$http){
    function otp(){
        sessionStorage.setItem("otp",true);
        return sessionStorage.getItem("otp");
    }
    $scope.subFunction1=function(){
            var value=Math.floor(Math.random() * 10000-1+1)+1;
            url="https://www.fast2sms.com/dev/bulk?authorization=d7tJOo1Ea6cUlymPGjwbBAFMqsxHgfpSkN8uXTQRIV3KriC5hZHDLX1xlJA527qMcQYt98fzENW0VjuF&sender_id=FSTSMS&language=english&route=qt&numbers=6386845062&message=33677&variables={AA}&variables_values="+value.toString();
        
            console.log(url)
            
            $http.get(url).then(function (response) {
                if(response.data){
                    sessionStorage.setItem("otp",value);
                    sessionStorage.setItem("phone",$scope.phone);
                    var data={"otp":value,"phone":$scope.phone}
                         $http.post("http://127.0.0.1:8000/amazing/otp_save/",JSON.stringify(data)).then(function(response){
                             if(response.data)
                             console.log("otp saved");
                             window.location.href="otp.html";
                         })
                    }
                        
                    },function(){
                    alert("message not sent");
                    }
                    )
                                    
                }
                
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