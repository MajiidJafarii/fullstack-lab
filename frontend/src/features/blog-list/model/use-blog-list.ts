import {
  useBlogPostsList,
} from "@/entities/blog"



export function useBlogList(
  page = 1,
) {


  return useBlogPostsList({

    page,

  })


}
