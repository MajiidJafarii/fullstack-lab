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
  useVerifyEmailAction,
} from "../model/use-verify-email"





export function VerifyCodeForm({

  email,

  onSuccess,

}: {

  email:string

  onSuccess?:()=>void

}) {



  const [
    code,
    setCode,
  ] = useState("")



  const {
    verifyEmail,
    isPending,
    error,
  } = useVerifyEmailAction()





  async function submit(

    e:React.FormEvent

  ){


    e.preventDefault()



    await verifyEmail({

      email,

      code,

    })



    onSuccess?.()


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

          کد ۶ رقمی ارسال شده به ایمیل

        </Label>



        <Input


          value={code}


          maxLength={6}


          onChange={(e)=>

            setCode(

              e.target.value

            )

          }


          className="

          h-12

          rounded-xl

          bg-slate-100

          border-0

          text-center

          text-xl

          tracking-[0.5em]

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

            کد تایید صحیح نیست

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
        "

      >

        {

          isPending

          ?

          "در حال تایید..."

          :

          "تایید ایمیل"

        }


      </Button>



    </form>


  )

}
