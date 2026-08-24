import {
  ArrowRight,
} from "lucide-react"


import {
  useNavigate,
  useParams,
} from "react-router"


import {
  useBlogPostsRetrieve,
} from "@/entities/blog"


import {
  useAuth,
} from "@/entities/session"


import {
  CommentForm,
} from "@/features/create-comment"


import {
  CommentSection,
} from "@/widgets/comment-section"





export function PostDetailPage() {


  const navigate = useNavigate()


  const {
    id,
  } = useParams()



  const {
    authenticated,
  } = useAuth()





  const {

    data: post,

    isLoading,

    isError,

  } = useBlogPostsRetrieve(

    Number(id)

  )





  if (isLoading) {

    return (

      <div
        dir="rtl"
        className="p-8"
      >

        در حال دریافت مطلب...

      </div>

    )

  }





  if (isError || !post) {

    return (

      <div
        dir="rtl"
        className="p-8"
      >

        مطلب پیدا نشد

      </div>

    )

  }





  return (

    <main

      dir="rtl"

      className="

      mx-auto

      max-w-5xl

      space-y-8

      px-5

      py-10

      "

    >



      <button

        onClick={() =>
          navigate(-1)
        }

        className="

        flex

        items-center

        gap-2

        rounded-2xl

        border

        border-border

        bg-card

        px-5

        py-3

        font-bold

        shadow-sm

        "

      >

        <ArrowRight size={18}/>

        برگشت

      </button>





      <article

        className="

        rounded-3xl

        border

        border-border

        bg-card

        p-8

        shadow-sm

        "

      >


        <h1

          className="

          text-4xl

          font-black

          leading-loose

          "

        >

          {post.title}

        </h1>




        <div

          className="

          mt-4

          text-sm

          text-muted-foreground

          "

        >

          {post.created_at}

        </div>




        <div

          className="

          mt-10

          whitespace-pre-line

          leading-10

          "

        >

          {post.content}

        </div>



      </article>





      <section

        className="space-y-8"

      >


        <CommentSection

          postId={post.id}

        />



        {

          authenticated

          ?

          (

            <CommentForm

              postId={post.id}

            />

          )

          :

          (

            <div

              className="

              rounded-3xl

              border

              border-border

              bg-card

              p-6

              text-center

              text-muted-foreground

              "

            >

              برای ارسال دیدگاه ابتدا وارد حساب کاربری شوید.


            </div>

          )

        }



      </section>



    </main>

  )

}
