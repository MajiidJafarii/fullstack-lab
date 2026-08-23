import {
  useBlogPostsCreate,
} from "@/entities/blog"



export function useCreatePost() {


  const mutation = useBlogPostsCreate()



  return {

    createPost:
      mutation.mutateAsync,


    isPending:
      mutation.isPending,


    error:
      mutation.error,


  }

}
