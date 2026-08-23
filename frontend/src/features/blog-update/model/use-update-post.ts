import {
  useBlogPostsPartialUpdate,
} from "@/entities/blog"


export function useUpdatePost() {


  const mutation =
    useBlogPostsPartialUpdate()



  return {

    updatePost:
      mutation.mutateAsync,


    isPending:
      mutation.isPending,


    error:
      mutation.error,

  }

}
