import {
  useQueryClient,
} from "@tanstack/react-query"


import {
  useBlogCommentsHideCreate,
  getBlogCommentsListQueryKey,
} from "@/entities/blog"





export function useHideComment() {


  const queryClient =
    useQueryClient()



  const mutation =
    useBlogCommentsHideCreate()





  async function hide(

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

    hide,

    isPending:
      mutation.isPending,

  }


}
