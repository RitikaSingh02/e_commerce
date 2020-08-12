angular.module("user_otp",[]).controller("user_otp_ctrl",function($scope,$http){
$scope.subFunction1=function(){
    var value=Math.floor(Math.random() * 10000-1+1)+1;
    url="https://www.fast2sms.com/dev/bulk?authorization=d7tJOo1Ea6cUlymPGjwbBAFMqsxHgfpSkN8uXTQRIV3KriC5hZHDLX1xlJA527qMcQYt98fzENW0VjuF&sender_id=FSTSMS&language=english&route=qt&numbers=6386845062&message=YOUR_QT_TEMPLATE_ID&variables={BB}&variables_values="+value.toString();

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