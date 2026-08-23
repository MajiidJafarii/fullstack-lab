import {
  PostList,
} from "@/features/blog-list"





export function HomePage() {


  return (

    <div

      dir="rtl"

      className="

      min-h-screen

      px-6

      py-8

      "

    >


      <section

        className="

        space-y-6

        "

      >



        <h1

          className="

          text-3xl

          font-black

          text-card-foreground

          "

        >

          آخرین مطالب


        </h1>




        <PostList />


      </section>


    </div>

  )

}
