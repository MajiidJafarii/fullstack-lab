import {
  Routes,
  Route,
} from "react-router"



import {
  AppLayout,
} from "./layout/app-layout"



import {
  HomePage,
} from "@/pages/home"



import {
  DashboardPage,
} from "@/pages/dashboard"



import {
  SettingsPage,
} from "@/pages/settings"



import {
  BlogPage,
} from "@/pages/blog"



import {
  PostDetailPage,
} from "@/pages/post-detail"





export function App() {


  return (


    <Routes>


      <Route

        element={

          <AppLayout />

        }

      >



        <Route

          path="/"

          element={

            <HomePage />

          }

        />



        <Route

          path="/dashboard"

          element={

            <DashboardPage />

          }

        />



        <Route

          path="/blog"

          element={

            <BlogPage />

          }

        />



        <Route

          path="/blog/:id"

          element={

            <PostDetailPage />

          }

        />



        <Route

          path="/profile"

          element={


            <div

              dir="rtl"

              className="min-h-screen px-5 py-8"

            >

              <section

                className="rounded-3xl border border-border bg-card p-6 shadow-sm"

              >

                <h1

                  className="text-2xl font-bold text-foreground"

                >

                  پروفایل

                </h1>


              </section>


            </div>


          }

        />



        <Route

          path="/settings"

          element={

            <SettingsPage />

          }

        />


      </Route>


    </Routes>


  )

}
