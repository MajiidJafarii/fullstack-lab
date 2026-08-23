import {
  useMeChangePasswordCreate,
} from "@/shared/api"



export function useChangePasswordAction(){


  const mutation =
    useMeChangePasswordCreate()



  async function changePassword(

    data: {

      current_password: string

      new_password: string

      new_password_confirm: string

    }

  ){


    return mutation.mutateAsync({

      data,

    })


  }





  return {


    changePassword,


    isPending:
      mutation.isPending,


    error:
      mutation.error,


    isSuccess:
      mutation.isSuccess,


  }


}
