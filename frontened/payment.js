angular.module("payment",[]).controller("payment_ctrl",function($scope,$http){
    $scope.errorMessage = false;
    $scope.subFunction=function(){
        
        var url="https://ifsc.razorpay.com/"+$scope.ifsc
        $http.get(url).then(function(response){
            
            if(response.data ){
                pass
            }     
        },function(response){
            $scope.errorMessage = "invalid ifsc";
        });
    }
})