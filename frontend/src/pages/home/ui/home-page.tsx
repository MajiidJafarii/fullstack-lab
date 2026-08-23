export function HomePage() {


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

        p-8

        shadow-sm

        transition-colors

        "

      >



        <h1

          className="

          text-3xl

          font-bold

          text-foreground

          "

        >

          سامانه مدیریت سازمانی

        </h1>



        <p

          className="

          mt-4

          leading-8

          text-muted-foreground

          "

        >

          خوش آمدید. از این بخش می‌توانید به امکانات سامانه دسترسی داشته باشید.

        </p>



      </section>






      <section

        className="

        mt-8

        grid

        gap-5

        md:grid-cols-3

        "

      >



        {
          [

            {
              title:"کاربران",

              text:"مدیریت اعضا و سطح دسترسی"

            },


            {
              title:"گزارش‌ها",

              text:"مشاهده گزارش‌های سیستم"

            },


            {
              title:"تنظیمات",

              text:"مدیریت تنظیمات حساب"

            },


          ].map((item)=>(



            <div

              key={item.title}

              className="

              rounded-2xl

              border

              border-border

              bg-card

              p-6


              shadow-sm


              transition-all


              hover:-translate-y-1

              hover:shadow-md


              "

            >



              <h2

                className="

                text-xl

                font-bold

                text-foreground

                "

              >

                {item.title}


              </h2>




              <p

                className="

                mt-3

                text-sm

                text-muted-foreground

                "

              >

                {item.text}


              </p>



            </div>



          ))

        }



      </section>



    </main>

  )

}
