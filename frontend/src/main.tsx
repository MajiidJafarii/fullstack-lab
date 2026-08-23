import React from "react"

import "@fontsource/vazirmatn/400.css"
import "@fontsource/vazirmatn/500.css"
import "@fontsource/vazirmatn/700.css"
import ReactDOM from "react-dom/client"


import {
  BrowserRouter,
} from "react-router"



import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query"



import {
  App,
} from "@/app/app"



import {
  AuthProvider,
} from "@/entities/session"



import {
  ThemeProvider,
} from "@/shared/theme"



import "./index.css"



const queryClient =
  new QueryClient()



ReactDOM
  .createRoot(
    document.getElementById("root")!
  )
  .render(


    <React.StrictMode>


      <QueryClientProvider

        client={queryClient}

      >


        <ThemeProvider>


          <BrowserRouter>


            <AuthProvider>


              <App />


            </AuthProvider>


          </BrowserRouter>


        </ThemeProvider>


      </QueryClientProvider>


    </React.StrictMode>


  )
