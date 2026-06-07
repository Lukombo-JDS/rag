package test

import (
	"api-gateaway-go/handlers"
	"api-gateaway-go/test/route"
	"testing"
)

var METHODS = []string{"GET","POST","PUT","PATCH","DELETE"}

type runTest struct{
	methods []string
	expected any
}


func (rT runTest)TestRouting(t *testing.T){

	trt := route.TestRouteTemplate{}
	trt.NewServerToTest()
	trt.TestingVariable = t

	for _,route := range trt.Routes {
		// t := trt.TestingVariable
		data := trt.Data
		// println("ROUTE TO TEST: ",route.Pattern)
		trt.Routing(trt.TestingVariable, trt.HttpMethods,data, route.Pattern, rT.expected)

	}
}



func TestMain(t *testing.T){
	var runTest runTest
	// var methods []string

	//Unit Tests
	//Public routes

	//Health
	runTest.expected = handlers.HEALTH_RESPONSE
	runTest.TestRouting(t)
	

	//Ready
	runTest.expected = handlers.READY_RESPONSE
	runTest.TestRouting(t)

}
