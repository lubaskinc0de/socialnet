import { createSlice } from '@reduxjs/toolkit';
import { getPosts, postLike } from '../../actions/postsActions';

const postsSlice = createSlice({
    name: 'postsSlice',
    initialState: {
        posts: [],
        nextPage: 1,
        loading: null,
        rejected: null,
        likePendingPosts: {},
        postsFilters: {
            priority: null,
            ordering: null,
        },
    },

    reducers: {
        setPostsPriority(state, action) {
            const { priority } = action.payload;

            if (state.postsFilters.priority !== priority) {
                // refresh

                state.posts = [];
                state.nextPage = 1;
            }

            state.postsFilters.priority = priority;
        },

        setPostsOrdering(state, action) {
            const { ordering } = action.payload;

            if (state.postsFilters.ordering !== ordering) {
                // refresh

                state.posts = [];
                state.nextPage = 1;
            }

            state.postsFilters.ordering = ordering;
        },
    },

    extraReducers: {
        // getPosts
        [getPosts.pending](state) {
            state.loading = true;
            state.rejected = false;
        },

        [getPosts.fulfilled](state, action) {
            const { posts, nextPage } = action.payload;

            const page = nextPage
                ? parseInt(
                      nextPage
                          .split('?')
                          .find((el) => el.includes('page'))
                          .split('=')[1]
                  )
                : null;

            if (posts.length) {
                state.posts = state.posts.concat(posts);
            }
            state.nextPage = page;
            state.loading = false;
        },

        [getPosts.rejected](state, action) {
            const { errorCode } = action.payload;

            state.loading = false;

            if (!(errorCode === 401)) {
                state.rejected = true;
            }
        },

        // postLike
        [postLike.pending](state, action) {
            const { arg: post_id } = action.meta;
            state.likePendingPosts[post_id] = null;
        },

        [postLike.fulfilled](state, action) {
            const { action: actionType, id: post_id } = action.payload;
            const post = state.posts.find(({ id }) => post_id === id);

            const isAdd = actionType === 'add';

            delete state.likePendingPosts[post_id];

            post.is_user_liked_post = isAdd;
            post.liked_count += isAdd ? 1 : -1;
        },

        [postLike.rejected](state, action) {
            const { id: post_id } = action.payload;
            delete state.likePendingPosts[post_id];
        },
    },
});

export const { setPostsPriority, setPostsOrdering } = postsSlice.actions;

export default postsSlice.reducer;
