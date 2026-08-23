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
  useRegisterAction,
} from "../model/use-register"





export function RegisterForm({

  onSuccess,

}: {

  onSuccess?: (email: string) => void

}) {



  const [
    username,
    setUsername,
  ] = useState("")



  const [
    email,
    setEmail,
  ] = useState("")



  const [
    password,
    setPassword,
  ] = useState("")



  const [
    confirmPassword,
    setConfirmPassword,
  ] = useState("")





  const {
    register,
    isPending,
    error,
  } = useRegisterAction()






  async function submit(

    e: React.FormEvent

  ) {


    e.preventDefault()



    if (

      password !== confirmPassword

    ) {

      return

    }






    await register({

      username,

      email,

      password,

      password_confirm:
        confirmPassword,

    })






    onSuccess?.(email)



  }






  return (


    <form

      onSubmit={submit}

      className="
      space-y-5
      "

    >





      <div className="space-y-2">

        <Label>

          نام کاربری

        </Label>


        <Input

          value={username}

          onChange={(e) =>
            setUsername(e.target.value)
          }

          className="
          h-12
          rounded-xl
          bg-slate-100
          border-0
          dark:bg-slate-800
          "

        />


      </div>






      <div className="space-y-2">


        <Label>

          ایمیل

        </Label>



        <Input

          type="email"

          value={email}

          onChange={(e) =>
            setEmail(e.target.value)
          }


          className="
          h-12
          rounded-xl
          bg-slate-100
          border-0
          dark:bg-slate-800
          "

        />


      </div>







      <div className="space-y-2">


        <Label>

          رمز عبور

        </Label>



        <Input

          type="password"

          value={password}

          onChange={(e) =>
            setPassword(e.target.value)
          }


          className="
          h-12
          rounded-xl
          bg-slate-100
          border-0
          dark:bg-slate-800
          "

        />


      </div>








      <div className="space-y-2">


        <Label>

          تکرار رمز عبور

        </Label>



        <Input

          type="password"

          value={confirmPassword}

          onChange={(e) =>
            setConfirmPassword(e.target.value)
          }


          className="
          h-12
          rounded-xl
          bg-slate-100
          border-0
          dark:bg-slate-800
          "

        />


      </div>







      {
        error ? (

          <div

            className="
            rounded-xl
            bg-red-50
            p-3
            text-sm
            text-red-700
            dark:bg-red-950
            dark:text-red-300
            "

          >

            خطا در ثبت نام، اطلاعات را بررسی کنید


          </div>


        ) : null

      }







      <Button

        disabled={isPending}

        className="
        h-12
        w-full
        rounded-xl
        bg-[#102a43]
        text-white
        hover:bg-[#163b63]
        "

      >

        {

          isPending

          ?

          "در حال ثبت نام..."

          :

          "ثبت نام"

        }


      </Button>





    </form>


  )

}
