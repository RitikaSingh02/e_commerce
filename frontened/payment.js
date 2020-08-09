angular.module("payment",[]).controller("payment_ctrl",function($scope,$http){

    $scope.subFunction=function(){
        
        var url="https://ifsc.razorpay.com/"+$scope.ifsc
        $http.get(url).then(function(response){
            
            if(response.data ){
                alert("correct ifsc");
            }     
        },function(response){
            alert("wrong ifsc");
        });
    }
})