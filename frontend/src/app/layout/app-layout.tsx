import {
  Outlet,
} from "react-router"


import {
  Sidebar,
} from "@/widgets/sidebar"


import {
  Header,
} from "@/widgets/header"



export function AppLayout() {

  return (

    <>

      <Header />

      <Sidebar />


      <main>

        <Outlet />

      </main>


    </>

  )
}
