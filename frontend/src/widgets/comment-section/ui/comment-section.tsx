import {
  CalendarDays,
  User,
} from "lucide-react"


import {
  useBlogCommentsList,
} from "@/entities/blog"


import {
  useAuth,
} from "@/entities/session"


import {
  useApproveComment,
} from "@/features/approve-comment"


import {
  useHideComment,
} from "@/features/hide-comment"





export function CommentSection({

  postId,

}: {

  postId: number

}) {



  const {
    user,
  } = useAuth()





  const {
    approve,
    isPending: approvePending,
  } = useApproveComment()





  const {
    hide,
    isPending: hidePending,
  } = useHideComment()





  const {

    data,

    isLoading,

  } = useBlogCommentsList({

    post: postId,

  })





  const comments =
    data?.results ?? []





  if (isLoading) {

    return (

      <div
        dir="rtl"
        className="text-muted-foreground"
      >

        در حال دریافت دیدگاه‌ها...

      </div>

    )

  }





  if (comments.length === 0) {

    return (

      <div

        dir="rtl"

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

        هنوز دیدگاهی ثبت نشده است.

      </div>

    )

  }





  return (

    <section

      dir="rtl"

      className="space-y-5"

    >


      <h2

        className="

        text-2xl

        font-black

        "

      >

        دیدگاه‌ها

      </h2>





      {

        comments.map(

          (comment) => (

            <article

              key={comment.id}

              className="

              rounded-3xl

              border

              border-border

              bg-card

              p-5

              shadow-sm

              "

            >



              <div

                className="

                mb-3

                flex

                items-center

                justify-between

                "

              >


                <div

                  className="

                  flex

                  items-center

                  gap-2

                  font-bold

                  "

                >

                  <User size={16}/>

                  {comment.user}

                </div>




                <div

                  className="

                  flex

                  items-center

                  gap-2

                  text-xs

                  text-muted-foreground

                  "

                >

                  <CalendarDays size={14}/>

                  {comment.created_at}

                </div>


              </div>





              <p

                className="

                leading-8

                text-muted-foreground

                "

              >

                {comment.content}

              </p>







              {

                user?.is_superuser

                &&

                !comment.is_approved

                &&

                (

                  <button

                    onClick={() =>
                      approve(comment.id)
                    }


                    disabled={approvePending}


                    className="

                    mt-5

                    rounded-xl

                    bg-green-600

                    px-5

                    py-2

                    font-bold

                    text-white

                    hover:bg-green-700

                    disabled:opacity-50

                    "

                  >

                    {

                      approvePending

                      ?

                      "در حال انتشار..."

                      :

                      "انتشار کامنت"

                    }


                  </button>

                )

              }







              {

                user?.is_superuser

                &&

                comment.is_approved

                &&

                (

                  <button

                    onClick={() =>
                      hide(comment.id)
                    }


                    disabled={hidePending}


                    className="

                    mr-3

                    mt-5

                    rounded-xl

                    bg-red-600

                    px-5

                    py-2

                    font-bold

                    text-white

                    hover:bg-red-700

                    disabled:opacity-50

                    "

                  >

                    {

                      hidePending

                      ?

                      "در حال مخفی کردن..."

                      :

                      "مخفی کردن کامنت"

                    }


                  </button>

                )

              }





              {

                user?.is_superuser

                &&

                !comment.is_approved

                &&

                (

                  <span

                    className="

                    mr-3

                    rounded-full

                    bg-yellow-100

                    px-3

                    py-1

                    text-xs

                    text-yellow-700

                    "

                  >

                    در انتظار تایید

                  </span>

                )

              }



            </article>

          )

        )

      }


    </section>

  )

}
