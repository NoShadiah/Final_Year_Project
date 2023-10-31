// import Home from "./pages/home/home";
// import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
// import Users from "./pages/users/users";
// import Products from "./pages/products/products";
// import Navbar from "./components/navbar/navbar";
// import Footer from "./components/footer/footer";
// import Menu from "./components/menu/menu";
// import Login from "./pages/login/Login";
// import "./styles/global.scss";
// import User from "./pages/user/User";
// import Product from "./pages/product/Product";
// // import {
// //   useQueryClient,
// //   QueryClientProvider,
// // } 
// // from "@tanstack/react-query";


// // const queryClient = QueryClient();

// function App() {
//   const Layout = () => {
//     return (
//       <div className="main">
//         <Navbar />
//         <div className="container">
//           <div className="menuContainer">
//             <Menu />
//           </div>
//           <div className="contentContainer">
//             {/* <QueryClientProvider client={queryClient}> */}
//               <Outlet />
//             {/* </QueryClientProvider> */}
//           </div>
//         </div>
//         <Footer />
//       </div>
//     );
//   };

//   const router = createBrowserRouter([
//     {
//       path: "/",
//       element: <Layout />,
//       children: [
//         {
//           path: "/",
//           element: <Home />,
//         },
//         {
//           path: "/users",
//           element: <Users />,
//         },
//         {
//           path: "/products",
//           element: <Products />,
//         },
//         {
//           path: "/users/:id",
//           element: <User />,
//         },
//         {
//           path: "/products/:id",
//           element: <Product />,
//         },
//       ],
//     },
//     {
//       path: "/login",
//       element: <Login />,
//     },
//   ]);

//   return <RouterProvider router={router} />;
// }

// export default App;
