import {
  useAuthVerifyEmailCreate,
} from "@/shared/api"



export function useVerifyEmailAction(){


  const mutation =
    useAuthVerifyEmailCreate()



  async function verifyEmail(

    data: {

      email: string

      code: string

    }

  ){


    return mutation.mutateAsync({

      data,

    })


  }





  return {

    verifyEmail,


    isPending:
      mutation.isPending,


    error:
      mutation.error,

  }


}
