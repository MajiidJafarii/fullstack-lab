import {
  useState,
} from "react"



import {
  PostCard,
} from "@/entities/blog"



import {
  useBlogList,
} from "../model/use-blog-list"





export function PostList() {


  const [
    page,
    setPage,
  ] = useState(1)



  const {
    data,
    isLoading,
    isError,
  } = useBlogList(page)





  if (isLoading) {

    return (

      <div>

        در حال دریافت پست‌ها...

      </div>

    )

  }





  if (isError) {

    return (

      <div>

        خطا در دریافت پست‌ها

      </div>

    )

  }





  const posts =
    data?.results ?? []





  if (posts.length === 0) {

    return (

      <div>

        پستی وجود ندارد

      </div>

    )

  }





  return (

    <div

      className="
      space-y-8
      "

    >


      <div

        className="
        grid
        gap-5
        sm:grid-cols-2
        lg:grid-cols-3
        xl:grid-cols-4
        "

      >

        {

          posts.map(

            (post) => (

              <PostCard

                key={post.id}

                post={post}

              />

            )

          )

        }

      </div>





      <div

        className="
        flex
        items-center
        justify-center
        gap-4
        "

      >


        <button

          disabled={!data?.previous}

          onClick={() =>
            setPage(
              (prev) =>
                Math.max(
                  prev - 1,
                  1
                )
            )
          }

          className="
          rounded-lg
          bg-slate-200
          px-4
          py-2
          disabled:opacity-50
          "

        >

          قبلی

        </button>





        <span>

          صفحه {page}

        </span>





        <button

          disabled={!data?.next}

          onClick={() =>
            setPage(
              (prev) =>
                prev + 1
            )
          }

          className="
          rounded-lg
          bg-slate-900
          px-4
          py-2
          text-white
          disabled:opacity-50
          "

        >

          بعدی

        </button>



      </div>



    </div>

  )

}
