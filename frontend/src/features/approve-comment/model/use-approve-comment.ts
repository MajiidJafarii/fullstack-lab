import {
  useQueryClient,
} from "@tanstack/react-query"


import {
  useBlogCommentsApproveCreate,
  getBlogCommentsListQueryKey,
} from "@/entities/blog"





export function useApproveComment() {


  const queryClient =
    useQueryClient()



  const mutation =
    useBlogCommentsApproveCreate()





  async function approve(

    id: number

  ) {


    await mutation.mutateAsync({

      id,

      data: {

        post: id,

        content: "",

      },

    })



    await queryClient.invalidateQueries({

      queryKey:
        getBlogCommentsListQueryKey(),

    })


  }





  return {

    approve,

    isPending:
      mutation.isPending,

  }


}
