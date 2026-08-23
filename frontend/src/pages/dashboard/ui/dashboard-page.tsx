import {
  useNavigate,
} from "react-router"


import {
  Button,
} from "@/shared/ui/button"


import {
  useAuth,
} from "@/entities/session"



export function DashboardPage() {

  const navigate = useNavigate()


  const {
    logout,
  } = useAuth()



  async function handleLogout() {

    await logout()

    navigate("/")

  }



  return (

    <main className="flex min-h-screen items-center justify-center p-8">

      <div className="space-y-4 text-center">

        <h1 className="text-3xl font-bold">
          داشبورد
        </h1>


        <Button
          onClick={handleLogout}
        >
          خروج
        </Button>


      </div>

    </main>

  )

}
