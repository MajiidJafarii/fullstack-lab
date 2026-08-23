import {
  PostList,
} from "@/features/blog-list"


import {
  CreatePostForm,
} from "@/features/blog-create"


import {
  useAuth,
} from "@/entities/session"





export function BlogPage() {


  const {
    user,
  } = useAuth()



  return (

    <div
      dir="rtl"
      className="
      space-y-8
      p-6
      "
    >


      <section>

        <h1 className="
        text-3xl
        font-bold
        ">

          بلاگ

        </h1>


        <p className="
        mt-2
        text-muted-foreground
        ">

          مشاهده نوشته‌ها و مدیریت پست‌ها

        </p>


      </section>




      {
        user?.is_superuser && (

          <CreatePostForm />

        )
      }





      <PostList />


    </div>

  )

}
