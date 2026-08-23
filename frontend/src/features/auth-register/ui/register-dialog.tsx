import {
  useState,
} from "react"



import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/shared/ui/dialog"



import {
  Button,
} from "@/shared/ui/button"



import {
  RegisterForm,
} from "./register-form"



import {
  VerifyCodeForm,
} from "./verify-code-form"





export function RegisterDialog(){


  const [
    open,
    setOpen,
  ] = useState(false)



  const [
    step,
    setStep,
  ] = useState<
    "register" | "verify"
  >("register")



  const [
    email,
    setEmail,
  ] = useState("")





  function close(){

    setOpen(false)

    setStep("register")

    setEmail("")

  }






  return (


    <Dialog

      open={open}

      onOpenChange={(value)=>{

        setOpen(value)

        if(!value){

          setStep("register")

        }

      }}

    >



      <DialogTrigger asChild>


        <Button

          variant="outline"

          className="

          h-10

          rounded-xl

          "

        >

          عضویت

        </Button>


      </DialogTrigger>





      <DialogContent

        dir="rtl"

        className="
        max-w-md
        rounded-3xl
        "

      >



        <DialogHeader>


          <DialogTitle>

            {

              step === "register"

              ?

              "ایجاد حساب کاربری"

              :

              "تایید ایمیل"

            }

          </DialogTitle>


        </DialogHeader>





        {

          step === "register"

          ?

          <RegisterForm

            onSuccess={(userEmail)=>{

              setEmail(userEmail)

              setStep("verify")

            }}

          />

          :

          <VerifyCodeForm

            email={email}

            onSuccess={close}

          />

        }



      </DialogContent>



    </Dialog>


  )

}
