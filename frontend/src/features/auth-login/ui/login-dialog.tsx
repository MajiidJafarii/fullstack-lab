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
  LoginForm,
} from "./login-form"



export function LoginDialog() {


  const [
    open,
    setOpen,
  ] = useState(false)



  return (

    <Dialog

      open={open}

      onOpenChange={setOpen}

    >


      <DialogTrigger asChild>


        <Button>

          ورود

        </Button>


      </DialogTrigger>




      <DialogContent

        className="
        bg-white
        text-black
        "

      >


        <DialogHeader>

          <DialogTitle>

            ورود به حساب

          </DialogTitle>


        </DialogHeader>



        <div

          className="
          block
          "

        >

          <LoginForm

            onSuccess={() =>
              setOpen(false)
            }

          />


        </div>



      </DialogContent>


    </Dialog>


  )

}
