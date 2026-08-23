import {
  useBlogPostsDestroy,
} from "@/entities/blog"



export function useDeletePost() {


  const mutation =
    useBlogPostsDestroy()



  return {

    deletePost:
      mutation.mutateAsync,


    isPending:
      mutation.isPending,

  }

}
