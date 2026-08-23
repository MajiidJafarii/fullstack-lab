import {
  useState,
} from "react"



import {
  Button,
} from "@/shared/ui/button"



import {
  Input,
} from "@/shared/ui/input"



import {
  Label,
} from "@/shared/ui/label"



import {
  useLoginAction,
} from "../model/use-login"





export function LoginForm({

  onSuccess,

}: {

  onSuccess?: () => void

}) {



  const [
    email,
    setEmail,
  ] = useState("")



  const [
    password,
    setPassword,
  ] = useState("")



  const {
    login,
    isPending,
    error,
  } = useLoginAction()






  async function submit(

    event: React.FormEvent

  ) {


    event.preventDefault()



    try {


      await login(

        email,

        password

      )



      onSuccess?.()



    } catch {

    }


  }





  return (


    <form

      onSubmit={submit}

      className="
      space-y-6
      "

    >



      <div

        className="
        space-y-2
        "

      >


        <Label

          className="
          text-sm
          font-medium
          text-slate-700
          dark:text-slate-200
          "

        >

          ایمیل


        </Label>



        <Input


          type="email"


          value={email}



          onChange={(e)=>
            setEmail(e.target.value)
          }



          className="

          h-12

          rounded-xl


          bg-slate-100


          border-0


          px-4


          text-base


          shadow-sm


          focus-visible:ring-2


          focus-visible:ring-[#c8a951]


          dark:bg-slate-800

          "


        />


      </div>






      <div

        className="
        space-y-2
        "

      >



        <Label

          className="
          text-sm
          font-medium
          text-slate-700
          dark:text-slate-200
          "

        >

          رمز عبور


        </Label>





        <Input


          type="password"



          value={password}



          onChange={(e)=>

            setPassword(

              e.target.value

            )

          }




          className="

          h-12

          rounded-xl


          bg-slate-100


          border-0


          px-4


          text-base


          shadow-sm


          focus-visible:ring-2


          focus-visible:ring-[#c8a951]


          dark:bg-slate-800

          "


        />


      </div>








      {

        error ?

        (

          <div

            className="
            rounded-xl
            bg-red-50
            px-4
            py-3
            text-sm
            text-red-700
            dark:bg-red-950
            dark:text-red-300
            "

          >

            اطلاعات ورود صحیح نیست


          </div>

        )

        :

        null

      }








      <Button


        disabled={isPending}



        className="


        h-12


        w-full


        rounded-xl



        bg-[#102a43]



        text-white



        text-base



        shadow-md



        hover:bg-[#163b63]



        "

      >


        {

          isPending

          ?

          "در حال ورود..."

          :

          "ورود"

        }


      </Button>





    </form>



  )

}
