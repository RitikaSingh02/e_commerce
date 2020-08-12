var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $filter,$http) {
    $scope.mail=sessionStorage.getItem("mail");
    console.log($scope.mail)
    $http.get('http://127.0.0.1:8000/amazing/product_details/').then(function (response) {

        console.log(response.data);
        $scope.searchString=response.data;
        $scope.searchString2=$scope.searchString;
        $scope.$watch('search', function(val)
            { 
                $scope.searchString= $filter('filter')($scope.searchString2, val);
            });
})

$scope.subFunction=function(){
        
        
    $http.get('http://127.0.0.1:8000/amazing/user/logout/').then(function (response) {
        if(response.data)
        alert(response.data);
        
},function(){
        alert("error");
});
}

});