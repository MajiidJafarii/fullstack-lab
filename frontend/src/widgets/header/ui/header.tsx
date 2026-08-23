import {
  LoginDialog,
} from "@/features/auth-login"



import {
  RegisterDialog,
} from "@/features/auth-register"



import {
  ThemeToggle,
} from "@/features/theme-toggle"



import {
  useAuth,
} from "@/entities/session"





export function Header() {


  const {
    authenticated,
  } = useAuth()





  return (


    <div


      className="

      w-full

      flex

      items-center

      justify-end


      px-5

      pt-5

      pb-4


      "


    >




      <div


        className="

        flex

        flex-row-reverse


        items-center


        gap-3


        "


      >




        {

          !authenticated &&

          <>


            <LoginDialog />


            <RegisterDialog />


          </>


        }




        <ThemeToggle />



      </div>



    </div>


  )

}
