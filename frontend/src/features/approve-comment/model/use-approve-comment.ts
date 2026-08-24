import {
  useQueryClient,
} from "@tanstack/react-query"


import {
  useBlogCommentsApproveCreate,
  getBlogCommentsListQueryKey,
} from "@/shared/api/generated/blog/blog"





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

      data: {},

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
