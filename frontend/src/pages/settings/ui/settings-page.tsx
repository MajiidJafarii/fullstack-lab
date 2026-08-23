import {
  ChangePasswordForm,
} from "@/features/change-password"



export function SettingsPage(){


  return (


    <main

      dir="rtl"

      className="

      min-h-screen

      px-5

      py-8

      "

    >



      <section

        className="

        rounded-3xl

        border

        border-border

        bg-card

        p-6

        shadow-sm

        "

      >



        <h1

          className="

          text-2xl

          font-bold

          text-foreground

          "

        >

          تنظیمات حساب


        </h1>



        <p

          className="

          mt-2

          text-muted-foreground

          "

        >

          مدیریت امنیت و اطلاعات حساب کاربری


        </p>





        <div

          className="

          mt-8

          max-w-xl

          "

        >


          <ChangePasswordForm />


        </div>



      </section>



    </main>


  )

}
