package route

import (
	"api-gateaway-go/cmd"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/go-chi/chi/v5"
	"github.com/stretchr/testify/require"
)


type TestRouteTemplate struct{
	TestingVariable *testing.T
	HttpMethods []string
	Routes []chi.Route
	Data json.Decoder
	ErrTest []error
	Server *cmd.Server
	Result []string
}

func (trt *TestRouteTemplate)NewServerToTest(){
	trt.Server = cmd.CreateNewServer()

	trt.Server.MountHandlers()
	trt.Routes = trt.Server.Router.Routes()
}

func (trt *TestRouteTemplate)Routing(
				t *testing.T,
				methods []string,
				data json.Decoder,
				route string,
				expected any,
		){

	// trt.newServerToTest()
	// errTest := trt.ErrTest

	for _,m := range methods  {

		if m  == "GET" {
			req, _ := http.NewRequest(m, route, nil)

			response := ExecuteRequest(req, trt.Server)

	    // Check the response code
	    	CheckResponseCode(t, http.StatusOK, response.Code)

	    // We can use testify/require to assert values, as it is more convenient
	    	require.Equal(t, expected, response.Body.String())
			
		}

		if m == "POST" {

			req,_ := http.NewRequest(m, route, data.Buffered())

			response := ExecuteRequest(req, trt.Server)
			CheckResponseCode(t, http.StatusOK, response.Code)
			require.Equal(t, expected, response.Body.String())
		}

			if m == "PUT" {
				req,_ := http.NewRequest(m, route, data.Buffered())

			response := ExecuteRequest(req, trt.Server)
			CheckResponseCode(t, http.StatusOK, response.Code)
			require.Equal(t, expected, response.Body.String())

		}

		if m == "PATCH" {
			req,_ := http.NewRequest(m, route, data.Buffered())

			response := ExecuteRequest(req, trt.Server)
			CheckResponseCode(t, http.StatusOK, response.Code)
			require.Equal(t, expected, response.Body.String())

		}

		if m == "DELETE" {
			req, _ := http.NewRequest(m, route, nil)

			response := ExecuteRequest(req, trt.Server)
			CheckResponseCode(t, http.StatusOK, response.Code)
			require.Equal(t, expected, response.Body.String())
			

		}
		t.Log("Error Testing \v: \v", m, route)
	}

}

// executeRequest, creates a new ResponseRecorder
// then executes the request by calling ServeHTTP in the router
// after which the handler writes the response to the response recorder
// which we can then inspect.
func ExecuteRequest(req *http.Request, s *cmd.Server) *httptest.ResponseRecorder {
    rr := httptest.NewRecorder()
    s.Router.ServeHTTP(rr, req)

    return rr
}

// checkResponseCode is a simple utility to check the response code
// of the response
func CheckResponseCode(t *testing.T, expected, actual int) {
    if expected != actual {
        t.Errorf("Expected response code %d. Got %d\n", expected, actual)
    }
}

// func TestHealth(t *testing.T) {
//     // Create a New Server Struct
//     s := cmd.CreateNewServer()
//     // Mount Handlers
//     s.MountHandlers()

//     // Create a New Request
//     req, _ := http.NewRequest("GET", "/health", nil)

//     // Execute Request
//     response := ExecuteRequest(req, s)

//     // Check the response code
//     CheckResponseCode(t, http.StatusOK, response.Code)

//     // We can use testify/require to assert values, as it is more convenient
//     require.Equal(t, "Hello World!", response.Body.String())
// }
