angular.module("user_otp",[]).controller("user_otp_ctrl",function($scope,$http){
$scope.subFunction1=function(){
    
    url ="https://www.fast2sms.com/dev/bulkV2?authorization=d7tJOo1Ea6cUlymPGjwbBAFMqsxHgfpSkN8uXTQRIV3KriC5hZHDLX1xlJA527qMcQYt98fzENW0VjuF&message=This is a Django generated msg And the OTP is "+sessionStorage.getItem("otp")+"&language=english&route=q&numbers="+sessionStorage.getItem("phone");
    console.log(url)
    var data={"phone":sessionStorage.getItem("phone"),"otp":sessionStorage.getItem("otp")}
    $http.post("http://127.0.0.1:8000/amazing/user/otp/otp_verify/",JSON.stringify(data)).then(function (response) {
        
           
            if(response.data!="wrong"){
                
                alert("OTP VERIFIED SUCCESSFULLY");
                window.location.href="signup.html";
            }
            else
            alert("INCORRECT OTP");        
    
})}
}
);