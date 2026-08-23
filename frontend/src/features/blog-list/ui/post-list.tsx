import {
  PostCard,
} from "@/entities/blog"


import {
  useBlogList,
} from "../model/use-blog-list"





export function PostList() {


  const {
    data,
    isLoading,
    isError,
  } = useBlogList()





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





  if (!data || data.length === 0) {

    return (

      <div>

        پستی وجود ندارد

      </div>

    )

  }





  return (

    <div
      className="
      grid
      gap-5
      md:grid-cols-2
      "
    >

      {
        data.map(

          (post) => (

            <PostCard

              key={post.id}

              post={post}

            />

          )

        )
      }


    </div>

  )

}
