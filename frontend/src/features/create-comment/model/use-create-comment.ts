import {
  useQueryClient,
} from "@tanstack/react-query"


import {
  useBlogCommentsCreate,
  getBlogCommentsListQueryKey,
} from "@/entities/blog"





export function useCreateComment() {


  const queryClient =
    useQueryClient()



  const mutation =
    useBlogCommentsCreate()





  async function create(

    data: {

      post: number

      content: string

    }

  ) {


    const response =
      await mutation.mutateAsync({

        data,

      })



    await queryClient.invalidateQueries({

      queryKey:
        getBlogCommentsListQueryKey(),

    })



    return response

  }





  return {

    create,

    isPending:
      mutation.isPending,

    error:
      mutation.error,

  }


}
