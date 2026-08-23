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
  useChangePasswordAction,
} from "../model/use-change-password"





export function ChangePasswordForm(){


  const [
    oldPassword,
    setOldPassword,
  ] = useState("")



  const [
    newPassword,
    setNewPassword,
  ] = useState("")



  const [
    confirmPassword,
    setConfirmPassword,
  ] = useState("")




  const {

    changePassword,

    isPending,

    error,

    isSuccess,

  } = useChangePasswordAction()






  async function submit(

    e: React.FormEvent

  ){


    e.preventDefault()



    if(

      newPassword !== confirmPassword

    ){

      return

    }




    await changePassword({

      current_password:
        oldPassword,


      new_password:
        newPassword,


      new_password_confirm:
        confirmPassword,

    })


  }





  return (


    <form

      onSubmit={submit}

      className="

      space-y-5

      rounded-2xl

      border

      border-border

      bg-card

      p-6

      "

    >




      <div className="space-y-2">

        <Label>

          رمز فعلی

        </Label>


        <Input

          type="password"

          value={oldPassword}

          onChange={(e)=>

            setOldPassword(
              e.target.value
            )

          }

        />


      </div>






      <div className="space-y-2">


        <Label>

          رمز جدید

        </Label>



        <Input

          type="password"

          value={newPassword}

          onChange={(e)=>

            setNewPassword(
              e.target.value
            )

          }

        />


      </div>






      <div className="space-y-2">


        <Label>

          تکرار رمز جدید

        </Label>



        <Input

          type="password"

          value={confirmPassword}

          onChange={(e)=>

            setConfirmPassword(
              e.target.value
            )

          }

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

            تغییر رمز انجام نشد


          </div>


        ) : null

      }





      {
        isSuccess ? (

          <div

            className="
            rounded-xl
            bg-green-50
            p-3
            text-sm
            text-green-700
            dark:bg-green-950
            dark:text-green-300
            "

          >

            رمز عبور با موفقیت تغییر کرد


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

          "در حال تغییر..."

          :

          "تغییر رمز عبور"

        }


      </Button>




    </form>


  )

}
